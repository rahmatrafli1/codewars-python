def greek_comparator(lhs, rhs):
    # Assuming greek_alphabet is a tuple defined in the global namespace
    greek_alphabet = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
    
    # Check if lhs and rhs are valid Greek letters
    if lhs in greek_alphabet and rhs in greek_alphabet:
        return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
    else:
        raise ValueError("Invalid Greek letters provided")
