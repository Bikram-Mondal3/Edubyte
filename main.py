from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

# def plot_equation(equation, x_range=(-10, 10)):
#     x = np.linspace(x_range[0], x_range[1], 400)
#     y = eval(equation)

#     plt.figure(figsize=(8, 6))
#     plt.plot(x, y, label=f'y = {equation}')
#     plt.title('Graph of the Equation')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.axhline(0, color='black',linewidth=0.5)
#     plt.axvline(0, color='black',linewidth=0.5)
#     plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
#     plt.legend()
#     plt.savefig('static/image.png')

# equation = "np.cos(x)"
# plot_equation(equation)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 

