import numpy as np

# tabular value iteration algorithm
# note: it returns Q-values instead of values
def tabular_vi(T, R, args, pi=None):
    V = np.random.random_sample(T.shape[1])
    Q = np.random.random_sample(T.shape[0:2])
    done = False
    steps = args.steps
    while steps and not done:
        delta = 0
        Q_old = Q
        # assuming R[a][s][s'] is only a function like R[a][s]
        # Q = np.einsum('ijk,ijk->ij', T, R) + g*np.einsum('ijk,k->ij', T, V)
        Q = R + args.g*np.einsum('ijk,k->ij', T, V)
        if pi is None:
            V = Q.max(axis=0)
        else:
            V = np.einsum('ij,ji->j', Q, pi)
        delta = max(delta, np.linalg.norm(Q_old - Q))
        if delta < args.eps:
            done = True
        steps -= 1
    return Q, V

def tabular_q_learning():
    pass

def extreme_va_abstraction(Q, epsilon=1e-9):
    return (Q.max(axis=0) // epsilon, Q.argmax(axis=0))

def extreme_q_abstraction(Q, epsilon=1e-9):
    return (Q.max(axis=0) // epsilon)

def weighted_norm(A,w):
    return np.sqrt((w*A*A).sum())