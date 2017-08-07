import numpy as np

# defined named tuples
from gym_lock.common import TwoDConfig, wrapToMinusPiToPi


def get_adjoint(transform):
    rot = transform[:3, :3]
    trans = transform[:3, 3]

    matrix_rep = np.array([[0, -trans[2], trans[1]],
                           [trans[2], 0, -trans[0]],
                           [-trans[1], trans[0], 0]])

    res = np.zeros((6, 6))
    res[:3, :3] = res[3:, 3:] = rot
    res[:3, 3:] = matrix_rep.dot(rot)
    return res

def skew_sym_to_vector(matrix):
    # matrix is 3 x 3
    return np.array([matrix[2, 1], matrix[0, 2], matrix[1, 0]])


class InverseKinematics(object):
    def __init__(self, kinematic_chain, target, alpha=-0.05, eps=0.0001, lam=25):
        self.kinematic_chain = kinematic_chain
        self.target = target
        self.alpha = alpha
        self.eps = eps
        self.lam = lam

    def set_target(self, new_target):
        self.target = new_target

    def set_current_config(self, current_config):
        self.kinematic_chain = current_config

    def get_error(self, clamp=False, clamp_mag=1):
        err_mat = self.kinematic_chain.get_transform() \
                      .dot(np.linalg.inv(self.target.get_transform())) \
                  - np.eye(4)
        err_vec = np.zeros(6)
        err_vec[:3] = err_mat[:3, 3]
        err_vec[3] = err_mat[2, 2] + err_mat[2, 1] + err_mat[1, 1]
        err_vec[4] = err_mat[0, 0] + err_mat[0, 2] + err_mat[2, 2]
        err_vec[5] = err_mat[1, 1] + err_mat[1, 0] + err_mat[0, 0]

        if clamp:
            for i in range(0, len(err_vec)):
                if np.abs(err_vec[i]) > clamp_mag:
                    err_vec[i] = clamp_mag * np.sign(err_vec[i])
        return err_vec

    def get_delta_theta(self, alg='trans', clamp_delta=False, clamp_mag=True):
        jac = self.kinematic_chain.get_jacobian()

        if clamp_mag:
            err = self.get_error(clamp=True)
        else:
            err = self.get_error()


        if alg == 'trans':
            dtheta = jac.transpose().dot(err)
            dtheta = self.alpha * dtheta / max(1, np.linalg.norm(dtheta))
        elif alg == 'pinv':
            dtheta = np.linalg.pinv(jac).dot(err)
        elif alg == 'dls':
            jac_t = jac.transpose()
            dtheta = jac_t.dot(np.linalg.inv(jac.dot(jac_t)
                               + (self.lam ** 2) * np.eye(jac.shape[0]))).dot(err)
        if clamp_delta:
            dtheta[np.abs(dtheta) < self.eps] = 0

        return dtheta


class KinematicChain(object):
    def __init__(self, initial_configuration):
        self.configuration = initial_configuration
        self.chain = []
        for link in self.configuration:
            self.chain.append(KinematicLink(**link))

    def update_chain(self, new_config):
        assert len(new_config) * 2 - 1 == len(self.chain)

        # update baseframe
        self.chain[0].set_x(new_config[0].x)
        self.chain[0].set_y(new_config[0].y)
        self.chain[0].set_theta(new_config[0].theta)

        # update angles at each joint
        for i in range(1, len(new_config)):
            self.chain[2 * i - 1].set_theta(new_config[i].theta)

    def get_link_config(self):
        total_transform = np.eye(4)
        link_locations = []
        theta = 0
        for link in self.chain:
            # print link.get_transform()
            total_transform = total_transform.dot(link.get_transform())
            if link.screw is None:
                # link is a translation
                theta = np.arccos(total_transform[0, 0]) \
                        * np.sign(np.arcsin(total_transform[1, 0]))
                theta = wrapToMinusPiToPi(theta)
                link_locations.append(TwoDConfig(total_transform[:2, 3][0], total_transform[:2, 3][1], theta))
        return link_locations

    def get_transform(self):
        total_transform = np.eye(4)
        for link in self.chain:
            total_transform = total_transform.dot(link.get_transform())
        return total_transform

    def get_jacobian(self):
        transform = np.eye(4)
        jacobian = []
        for i in range(0, len(self.chain)):
            transform = transform.dot(self.chain[i].get_transform())
            if self.chain[i].screw is not None:
                # end of a link
                screw = self.chain[i].screw
                adj = get_adjoint(transform)
                jacobian_i = adj.dot(screw)
                jacobian.append(jacobian_i)
        return np.array(jacobian).transpose()


class KinematicLink(object):
    def __init__(self, theta=0, x=0, y=0, scale=1, screw=None, name='KinematicLink'):
        self.transform = np.asarray([[np.cos(theta), -np.sin(theta), 0, x],
                                     [np.sin(theta), np.cos(theta), 0, y],
                                     [0, 0, 1, 0],
                                     [0, 0, 0, scale]])
        self.theta = theta
        self.x = x
        self.y = y
        self.scale = scale
        self.screw = np.array(screw) if screw != None else None
        self.name = name

    def set_theta(self, theta):
        self.transform[:2, :2] = [[np.cos(theta), -np.sin(theta)],
                                  [np.sin(theta), np.cos(theta)]]
        self.theta = theta

    def set_x(self, x):
        self.transform[0, 3] = x
        self.x = x

    def set_y(self, y):
        self.transform[1, 3] = y
        self.y = y

    def set_scale(self, scale):
        self.transform[2, 3] = scale
        self.scale = scale

    def get_transform(self):
        return self.transform

    def get_omega(self):
        rot = self.transform[:3, :3]
        if np.allclose(np.eye(3), rot):
            # theta is 0
            omega = np.zeros(3)
        elif np.isclose(np.trace(rot), -1):
            # theta is pi
            if not np.isclose(rot[2, 2], -1):
                # axis is z axis
                factor = 1 / np.sqrt(2 * (1 + rot[2, 2]))
                omega = factor * np.array([rot[0, 2], rot[1, 2], 1 + rot[2, 2]])
        else:
            # theta in [0, pi)
            # rot[1, 0] is sin(theta)
            omega_m = 1 / (2 * rot[1, 0]) * (rot - rot.transpose())
            print omega_m
            omega = skew_sym_to_vector(omega_m)
        return omega





def main():
    # test get omega
    trans = KinematicLink(theta=1.55, x=5, y=10)
    print trans.get_omega()


if __name__ == "__main__":
    main()
