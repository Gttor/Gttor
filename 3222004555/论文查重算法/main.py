import sys


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def calculate_similarity(original_text, plagiarized_text):
    original_words = original_text.split()
    plagiarized_words = plagiarized_text.split()

    total_words = len(original_words)
    matching_words = sum(1 for word in plagiarized_words if word in original_words)

    similarity = matching_words / total_words * 100
    return similarity


def main():
    print("欢迎使用论文查重算法！")

    original_file_path = input("请输入原文文件的绝对路径：")
    plagiarized_file_path = input("请输入抄袭版论文文件的绝对路径：")
    output_file_path = input("请输入输出的答案文件的绝对路径：")

    original_text = read_file(original_file_path)
    plagiarized_text = read_file(plagiarized_file_path)

    similarity = calculate_similarity(original_text, plagiarized_text)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"{similarity:.2f}")

    print(f"论文查重完成！重复率为: {similarity:.2f}%，结果已保存到 {output_file_path}")


if __name__ == "__main__":
    main()
