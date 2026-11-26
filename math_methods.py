import numpy as np

def least_squares():
    """Placeholder for least squares method implementation."""
    pass

def linear_interpolation(x_values, y_values, x):
    """Linear interpolation method for estimating values between known data points."""
    
    # Ensure that the input arrays are numpy arrays for easier maniupulation

    x_values = np.array(x_values)
    y_values = np.array(y_values)

    # Find the indices of the interval that contains the input x value
    idx = np.searchsorted(x_values, x) - 1

    # Handle edge cases where x is outside the range of x values
    if x < 0 or x > 100:
        raise ValueError("Input x is outside the range of accepted x values (0 to 100).")

    # Perform linear interpolation using the two nearest data points
    x0, x1 = x_values[idx], x_values[idx + 1]
    y0, y1 = y_values[idx], y_values[idx + 1]

    m = (y1 - y0) / (x1 - x0)  # Calculate the slope
    y = y0 + m * (x - x0)  # Calculate the interpolated y value

    return y # Return the interpolated value
    

def bisection(func, a, b, tol=1e-5):
    """Bisection method for finding roots of a function over strictly increasing or decreasing sections."""

    xl = a
    xu = b
    xm = (xl + xu) / 2.0

    # Check if the difference between the upper and lower bounds is within the given tolerance
    if abs(xu - xl) < tol:
        return xm
    # If the difference between the bounds is not within tolerance, continue bisection
    else:
        # Checks current interval for a sign change
        if func(xm) * func(xl) < 0:
            # If the function changes sign between xl and xm, the root lies in that interval
            xu = xm
        else:
            # If the function does not change sign between xl and xm, the root lies in the other interval
            xl = xm

        # Recursively call the bisection method with the updated bounds
        return bisection(func, xl, xu, tol)

