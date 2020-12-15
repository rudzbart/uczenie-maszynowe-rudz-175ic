def create_output(w_bias, w1, w2, bias,x1, x2, activation, output):
    print("|w_bias: ", w_bias, " |w1: ",w1," |w2: ", w2," |bias: ",bias, " |x1: ", x1, " |x2: ", x2,
          " |Activation value: ",activation," |Output: ",output)

def activation_function(x):
    if x >= 0:
        return 1
    else:
        return 0

def neuron_output(w_bias, w1, w2, bias, x1, x2):
    return activation_function(activation_value(w_bias, w1, w2, bias, x1, x2))

def activation_value(w_bias, w1, w2, bias, x1, x2):
    return bias*w_bias+w1*x1+w2*x2

create_output(-1.5,1,1,1,0,0,activation_value(-1.5, 1, 1, 1, 0, 0),neuron_output(-1.5, 1, 1, 1, 0, 0))
create_output(-1.5,1,1,1,0,1,activation_value(-1.5, 1, 1, 1, 0, 1),neuron_output(-1.5, 1, 1, 1, 0, 1))
create_output(-1.5,1,1,1,1,0,activation_value(-1.5, 1, 1, 1, 1, 0),neuron_output(-1.5, 1, 1, 1, 1, 0))
create_output(-1.5,1,1,1,1,1,activation_value(-1.5, 1, 1, 1, 1, 1),neuron_output(-1.5, 1, 1, 1, 1, 1))

create_output(-0.5, 1, 1, 1, 0, 0,activation_value(-0.5, 1, 1, 1, 0, 0),neuron_output(-0.5, 1, 1, 1, 0, 0))
create_output(-0.5, 1, 1, 1, 0, 1,activation_value(-0.5, 1, 1, 1, 0, 1),neuron_output(-0.5, 1, 1, 1, 0, 1))
create_output(-0.5, 1, 1, 1, 1, 0,activation_value(-0.5, 1, 1, 1, 1, 0),neuron_output(-0.5, 1, 1, 1, 1, 0))
create_output(-0.5, 1, 1, 1, 1, 1,activation_value(-0.5, 1, 1, 1, 1, 1),neuron_output(-0.5, 1, 1, 1, 1, 1))

create_output(1, -2, 0, 1, 0, 0,activation_value(1, -2, 0, 1, 0, 0),neuron_output(1, -2, 0, 1, 0, 0))
create_output(1, -2, 0, 1, 1, 0,activation_value(1, -2, 0, 1, 1, 0),neuron_output(1, -2, 0, 1, 1, 0))

def xnor_network_output(x1, x2):
    notA_and_notB = neuron_output(0.5, -1, -1, 1, x1, x2)
    print("\nFirst layer data:\n(A’.B’):")
    create_output(0.5, -1, -1, 1, x1, x2, activation_value(0.5, -1, -1, 1, x1, x2),notA_and_notB)

    A_and_B = neuron_output(-1.5, 1, 1, 1, x1, x2)

    print("(A.B):")
    create_output(-1.5, 1, 1, 1, x1, x2,activation_value(-1.5, 1, 1, 1, x1, x2),A_and_B)
    print("\nOutput data:")
    return neuron_output(-0.5, 1, 1, 1, notA_and_notB, A_and_B)

create_output(-1.5, 1, 1, 1, 0, 0,activation_value(-1.5, 1, 1, 1, 0, 0),xnor_network_output(0, 0))
create_output(-1.5, 1, 1, 1, 0, 1,activation_value(-1.5, 1, 1, 1, 0, 1),xnor_network_output(0, 1))
create_output(-1.5, 1, 1, 1, 1, 0,activation_value(-1.5, 1, 1, 1, 1, 0),xnor_network_output(1, 0))
create_output(-1.5, 1, 1, 1, 1, 1,activation_value(-1.5, 1, 1, 1, 1, 1),xnor_network_output(1, 1))

def xor_network_output(x1, x2):
    return neuron_output(1, -2, 0, 1, xnor_network_output(x1, x2), 0)

create_output(-1.5, 1, 1, 1, 0, 0,activation_value(-1.5, 1, 1, 1, 0, 0),xor_network_output(0, 0))
create_output(-1.5, 1, 1, 1, 0, 1,activation_value(-1.5, 1, 1, 1, 0, 1),xor_network_output(0, 1))
create_output(-1.5, 1, 1, 1, 1, 0,activation_value(-1.5, 1, 1, 1, 1, 0),xor_network_output(1, 0))
create_output(-1.5, 1, 1, 1, 1, 1,activation_value(-1.5, 1, 1, 1, 1, 1),xor_network_output(1, 1))