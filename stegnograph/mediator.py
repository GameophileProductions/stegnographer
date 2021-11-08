import PIL.Image
import os
# from PIL import ImageTk as itk


def encryption(box_image_path, container_image_path, encryption_output_path):
    size = 1920, 1080

    MAX_COLOR_VALUE = 256
    MAX_BIT_VALUE = 8

    def make_image(data, resolution):
        image = PIL.Image.new("RGB", resolution)
        image.putdata(data)
        return image

    def remove_n_least_significant_bits(value, n):
        value = value >> n
        return value << n

    def get_n_least_significant_bits(value, n):
        value = value << MAX_BIT_VALUE - n
        value = value % MAX_COLOR_VALUE
        return value >> MAX_BIT_VALUE - n

    def get_n_most_significant_bits(value, n):
        return value >> MAX_BIT_VALUE - n

    def shit_n_bits_to_8(value, n):
        return value << MAX_BIT_VALUE - n

    # this function accepts 1- box image file(not path) 2 - container image file (not path) 3- something realted to algorithm whose value is always supposed to be 2

    def encode(image_to_hide, image_to_hide_in, n_bits):
        width, height = image_to_hide.size

        hide_image = image_to_hide.load()
        hide_in_image = image_to_hide_in.load()

        data = []

        for y in range(height):
            for x in range(width):
                # (107, 3, 10)
                # most sig bits
                try:
                    pixel = hide_image[x, y]
                    r_hide, g_hide, b_hide = pixel[0], pixel[1], pixel[2]

                    r_hide = get_n_most_significant_bits(r_hide, n_bits)
                    g_hide = get_n_most_significant_bits(g_hide, n_bits)
                    b_hide = get_n_most_significant_bits(b_hide, n_bits)

                # remove lest n sig bits
                    pixel_in = hide_in_image[x, y]
                    r_hide_in, g_hide_in, b_hide_in = pixel_in[0], pixel_in[1], pixel_in[2]

                    r_hide_in = remove_n_least_significant_bits(
                        r_hide_in, n_bits)
                    g_hide_in = remove_n_least_significant_bits(
                        g_hide_in, n_bits)
                    b_hide_in = remove_n_least_significant_bits(
                        b_hide_in, n_bits)

                    data.append((r_hide + r_hide_in,
                                 g_hide + g_hide_in,
                                 b_hide + b_hide_in))

                except:
                    continue

        return make_image(data, image_to_hide.size)

    # this function accepts 1- the encrypted image file (not path) 2- container image file (not path) 3- something realted to algorithm whose value is always supposed to be 2

    box_image = PIL.Image.open(mode='r', fp=box_image_path)
    container_image = PIL.Image.open(mode='r', fp=container_image_path)
    encode(box_image, container_image, 2).save(encryption_output_path)


def decryption(encrypted_image_path, decryption_output_path):
    size = 1920, 1080

    MAX_COLOR_VALUE = 256
    MAX_BIT_VALUE = 8

    def make_image(data, resolution):
        image = PIL.Image.new("RGB", resolution)
        image.putdata(data)
        return image

    def remove_n_least_significant_bits(value, n):
        value = value >> n
        return value << n

    def get_n_least_significant_bits(value, n):
        value = value << MAX_BIT_VALUE - n
        value = value % MAX_COLOR_VALUE
        return value >> MAX_BIT_VALUE - n

    def get_n_most_significant_bits(value, n):
        return value >> MAX_BIT_VALUE - n

    def shit_n_bits_to_8(value, n):
        return value << MAX_BIT_VALUE - n

    def decode(image_to_decode, n_bits):
        width, height = image_to_decode.size
        encoded_image = image_to_decode.load()

        data = []

        for y in range(height):
            for x in range(width):
                r_encoded, g_encoded, b_encoded = encoded_image[x, y]

                r_encoded = get_n_least_significant_bits(r_encoded, n_bits)
                g_encoded = get_n_least_significant_bits(g_encoded, n_bits)
                b_encoded = get_n_least_significant_bits(b_encoded, n_bits)

                r_encoded = shit_n_bits_to_8(r_encoded, n_bits)
                g_encoded = shit_n_bits_to_8(g_encoded, n_bits)
                b_encoded = shit_n_bits_to_8(b_encoded, n_bits)

                data.append((r_encoded, g_encoded, b_encoded))

        return make_image(data, image_to_decode.size)

    encrypted_image = PIL.Image.open(mode='r', fp=encrypted_image_path)
    decode(encrypted_image, 2).save(decryption_output_path)
