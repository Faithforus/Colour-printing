from colour_printing.custom.markers import Markers
from colour_printing.custom.style import Back, Mode, Fore

default_info = "info"
default_warn = "warn"
default_success = "success"
default_error = "error"


class ColourPrint:
    Markers = Markers

    def __init__(self):
        self.__default_setting()

    def __init_subclass__(cls, **kwargs):
        cls.custom(cls)

    def custom(self):
        e = '''
        Custom styles need to override this method ! 
        for example : 
            self.debug = self.Markers('debug').flag_style(mode="bold").time_style(...)'''
        raise NotImplementedError(e)

    def __default_setting(self):
        self.info = Markers(default_info) \
            .flag_style(mode=Mode.BOLD, fore=Fore.BLUE).time_style(mode=Mode.INVERT).message_style(mode=Mode.BOLD,
                                                                                                   fore=Fore.BLUE)

        self.warn = Markers(default_warn) \
            .flag_style(mode=Mode.BOLD, fore=Fore.YELLOW).time_style(mode=Mode.INVERT).message_style(mode=Mode.BOLD,
                                                                                                     fore=Fore.YELLOW)

        self.success = Markers(default_success) \
            .flag_style(mode=Mode.BOLD, fore=Fore.GREEN).time_style(mode=Mode.INVERT).message_style(mode=Mode.BOLD,
                                                                                                    fore=Fore.GREEN)

        self.error = Markers(default_error) \
            .flag_style(mode=Mode.BOLD, fore=Fore.RED).time_style(mode=Mode.INVERT).message_style(mode=Mode.BOLD,
                                                                                                  fore=Fore.RED)

    def __str__(self):
        return """
                @'fore': # 前景色
                        'black': 黑色
                        'red': 红色
                        'green': 绿色
                        'yellow': 黄色
                        'blue':  蓝色
                        'purple':  紫红色
                        'cyan':  青蓝色
                        'white':  白色
                @'back':# 背景
                        'black':  黑色
                        'red':  红色
                        'green': 绿色
                        'yellow':  黄色
                        'blue': 蓝色
                        'purple':  紫红色
                        'cyan':  青蓝色
                        'white': 白色
                @'mode':# 显示模式
                        'normal': 终端默认设置
                        'bold':  高亮显示
                        'underline':  使用下划线
                        'blink': 闪烁
                        'invert': 反白显示
                        'hide': 不可见
            """


log = ColourPrint()
