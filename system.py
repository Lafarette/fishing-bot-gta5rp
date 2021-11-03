import mss
import ctypes
import time
import pyautogui as pg


def screenshot(output='screen.png'):
    with mss.mss() as sct:
        sct.shot(mon=1, output=output)


def write_key(hex_key_code: int, interval=0.1, pause=None):
    DIK_I = 0x17

    PUL = ctypes.POINTER(ctypes.c_ulong)

    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP = 0x0002
    KEYEVENTF_SCANCODE = 0x0008
    KEYEVENTF_UNICODE = 0x0004

    class KeyBdInput(ctypes.Structure):
        _fields_ = [
            ('wVk', ctypes.c_ushort),
            ('wScan', ctypes.c_ushort),
            ('dwFlags', ctypes.c_ulong),
            ('time', ctypes.c_ulong),
            ('dwExtraInfo', PUL)
        ]

    class HardwareInput(ctypes.Structure):
        _fields_ = [
            ('uMsg', ctypes.c_ulong),
            ('wParamL', ctypes.c_short),
            ('wParamH', ctypes.c_ushort)
        ]

    class MouseInput(ctypes.Structure):
        _fields_ = [
            ('dx', ctypes.c_long),
            ('dy', ctypes.c_long),
            ('mouseData', ctypes.c_ulong),
            ('dwFlags', ctypes.c_ulong),
            ('time', ctypes.c_ulong),
            ('dwExtraInfo', PUL)
        ]

    class Input_I(ctypes.Union):
        _fields_ = [
            ('ki', KeyBdInput),
            ('mi', MouseInput),
            ('hi', HardwareInput)
        ]

    class Input(ctypes.Structure):
        _fields_ = [
            ('type', ctypes.c_ulong),
            ('ii', Input_I)
        ]

    def press_key(hex_key_code: int):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hex_key_code, KEYEVENTF_SCANCODE,
                            0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def release_key(hex_key_code: int):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hex_key_code, KEYEVENTF_SCANCODE |
                            KEYEVENTF_KEYUP, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    press_key(hex_key_code)
    time.sleep(interval)
    release_key(hex_key_code)

    if pause:
        time.sleep(pause)


def get_settings():
    """Возвращает настройки для текущего разрешения: Координаты для скриншотов,
    имитаций нажатия кнопок мыши и т.д."""
    size_screen = pg.size()
    if size_screen in [(1280, 720), (1366, 768), (1600, 900), (1920, 1080), (2560, 1440)]:  # 16:9
        k = int(size_screen[0] / 960)
        settings = {
            'scale_factor': k,
            'scale_size': (960, 540),
            'path_templateMK2': 'Images/mk2_16at9_960x540.jpg',
            'path_templateNeedClick': 'Images/need_click_16at9_960x540.jpg',
            'path_templateEndFishing': 'Images/end_fishing_16at9_960x540.jpg'
        }
        return settings


