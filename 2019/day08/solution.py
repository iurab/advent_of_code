def get_input():
    with open('input') as file:
        line = file.readline()
    data = list(map(int, line))
    return data


def part01():
    size = 25 * 6
    pixels = get_input()
    layers = [pixels[i:i + size] for i in range(0, len(pixels), size)]
    zeros = [layer.count(0) for layer in layers]
    ok_layer = zeros.index(min(zeros))
    result = layers[ok_layer].count(1) * layers[ok_layer].count(2)
    print(result)


def part02():
    size = 25 * 6
    pixels = get_input()
    layers = [pixels[i:i + size] for i in range(0, len(pixels), size)]
    image = []
    for i in range(size):
        colors = [layer[i] for layer in layers]
        for color in colors:
            if color != 2:
                final_color = color
                break
        image.append(final_color)
    # Display result:
    for i in range(0, len(image), 25):
        line = ''.join(list(map(str,[chr(32) if image[j] == 0 else chr(35) for j in range(i,i+25)])))
        print(line)


if __name__ == '__main__':
    part01()
    part02()