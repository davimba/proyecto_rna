from fann2 import libfann

def entrenar():

    connection_rate = 1
    learning_rate = 0.7
    num_input = 400
    num_hidden = 50
    num_output = 5

    desired_error = 0.0001
    max_iterations = 100000
    iterations_between_reports = 1000

    ann = libfann.neural_net()
    ann.create_sparse_array(connection_rate, (num_input, num_hidden, num_output))
    ann.set_learning_rate(learning_rate)
    ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC_STEPWISE)
    ann.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC_STEPWISE)

    ann.train_on_file("patrones.data", max_iterations, iterations_between_reports, desired_error)

    ann.save("red.net")

def probar(array):

    ann = libfann.neural_net()
    ann.create_from_file("red.net")
    print ann.run(array)
    return ann.run(array)