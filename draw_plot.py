import matplotlib.pyplot as plt

def readInFile(file_name):
    data = [[],[]]
    f = open(file_name, 'r')
    for line in f.readlines():
        if line.__contains__("Loss"):
            loss = float(line.split(" ")[2])
            acc  = float((line.split(" ")[-1]).strip("(").strip("))\t\n"))
            data[0].append(loss)
            data[1].append(acc)

    return data

def draw_plot(data):

    # data[0] contains loss values and data[1] contains accuracy values
    loss_values = data[0]
    accuracy_values = data[1]

    # Plotting loss curve
    plt.figure(figsize=(10, 5))
    plt.plot(loss_values, label='Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss Curve')
    plt.legend()
    plt.show()

    # Plotting accuracy curve
    plt.figure(figsize=(10, 5))
    plt.plot(accuracy_values, label='Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Accuracy Curve')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    draw_plot(readInFile("log/log_gridTD_01.txt"))
    # readInFile("log.txt")