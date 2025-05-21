from PIL import Image
import random

# 🔒 Encrypt image by shuffling pixels using a secret key
def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = list(image.getdata())
    
    random.seed(key)  # Secret key makes the shuffle predictable
    random.shuffle(pixels)

    encrypted_img = Image.new(image.mode, image.size)
    encrypted_img.putdata(pixels)
    encrypted_img.save(output_path)
    print(f"✅ Image encrypted and saved as {output_path}")

# 🔓 Decrypt image using the same secret key
def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    encrypted_pixels = list(image.getdata())
    
    random.seed(key)
    index_map = list(range(len(encrypted_pixels)))
    random.shuffle(index_map)

    # Put pixels back in original order
    decrypted_pixels = [None] * len(encrypted_pixels)
    for i, j in enumerate(index_map):
        decrypted_pixels[j] = encrypted_pixels[i]

    decrypted_img = Image.new(image.mode, image.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save(output_path)
    print(f"✅ Image decrypted and saved as {output_path}")

# 🧠 Ask user what they want to do
def main():
    print("=== 🖼️ Image Encryptor/Decryptor ===")
    choice = input("Encrypt or Decrypt (e/d)? ").lower()
    key = input("Enter secret key: ")
    input_path = input("Enter input image path (like photo.png): ")
    output_path = input("Enter output image path (like encrypted.png): ")

    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    elif choice == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print("❌ Invalid choice. Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
