"""
本脚本为将输入的字符串转换为编码并输出，
以及将编码转译回小写字符串并输出。
功能包含：强制转换为小写字母、检测是否为小写字母、
        检测是否为字母、ACSII编码转换，以及翻译。
目前只支持英文字母转译。
"""


def encoded(password: str) -> list[int]:
    """
    本函数为：将输入的字母转换为(ACSII - 96）的一串数字码
    包含检测是否为小写字母，以及检测是否为字母
    错误将返回 ValueError
    :param password: 输入的字母字符串
    :return: 返回编码后的数字
    """
    if not password.islower() or not password.isalpha():
        raise ValueError("错误：仅支持小写字母（a ~ z）")
    return [ord(s) - 96 for s in password]


def decode(encoded: list[int]) -> str:
    """
    将编码之后的数字字符串解码回字母字符串。
    :param encoded: encoded函数返回的数字
    :return: 解码之后的字符串
    """
    return "".join(chr(s + 96) for s in encoded)


# ------------主程序--------------
def main(password: str) -> None:
    print(f"编码前为：{password}，编码之后为{encoded(password)}")
    print(f"解码前为：{encoded(password)}，解码之后为{decode(encoded(password))}")


def detect_input() -> None:
    print("编码开始")
    while True:
        user_input = input("请输入字母：").strip()
        if user_input.lower() == 'q':
            print("再见！")
            break
        try:
            main(user_input.lower())
        except ValueError as e:
            print(f"输入不合法: {e}")
        print("-" * 30)


if __name__ == '__main__':
    detect_input()
