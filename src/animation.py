import time


class Animation:
    """Класс для управления анимациями."""

    @staticmethod
    def animate_success(message: str) -> None:
        """Анимация успешного выполнения действия."""
        print(message, end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
