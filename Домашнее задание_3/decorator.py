import time

def repeat(call_count, start_sleep_time, factor, border_sleep_time):
    def my_decorator(func):
        def work_func():
            start = 0
            pause = start_sleep_time
            while start < call_count:
                print(f"Запуск номер {start+1}. Ожидание: {pause} секунд.")
                time.sleep(pause)
                func()
                pause *= pow(2, factor)
                if pause > border_sleep_time:
                    pause = border_sleep_time
                start += 1
        return work_func
    return my_decorator


@repeat(10, 1, 3, 2)
def pass_func():
    pass
