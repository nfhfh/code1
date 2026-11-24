"""一段随便写的小 Python 程序：终端进度条 + 埃氏质数筛 + 斐波那契。"""

import time


def progress_bar(step: int, total: int, width: int = 30) -> str:
    """按当前进度生成一个单行进度条的字符串。"""
    filled = int(width * step / total)
    bar = "#" * filled + "-" * (width - filled)
    percent = step / total * 100
    return f"\r[{bar}] {percent:6.2f}%  ({step}/{total})"


def prime_sieve(limit: int) -> list[int]:
    """用埃拉托斯特尼筛法返回 <= limit 的全部质数。"""
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            is_prime[p * p :: p] = [False] * len(is_prime[p * p :: p])
        p += 1
    return [n for n, flag in enumerate(is_prime) if flag]


def fib(n: int) -> list[int]:
    """返回斐波那契数列前 n 项。"""
    seq, a, b = [], 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def main() -> None:
    total = 30
    for i in range(total + 1):
        print(progress_bar(i, total), end="", flush=True)
        time.sleep(0.03)
    print()

    primes = prime_sieve(100)
    print(f"100 以内的质数共 {len(primes)} 个：{primes}")
    print("斐波那契前 15 项：", fib(15))


if __name__ == "__main__":
    main()
