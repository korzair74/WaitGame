import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


def time_result(a, b):
    result = round(float(a) - float(b), 3)
    if result > 0:
        print("Too Fast by " + str(result) + "s")
    elif result < 0:
        new_result = abs(result)
        print("Too Slow by " + str(new_result) + "s")
    else:
        print("Perfect! You Win!")


target_time = input("Enter target time:  ")
print("your target time is  " + target_time + "s")
input("---Press Enter to start---")
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
time_result(target_time, time_lapsed)
