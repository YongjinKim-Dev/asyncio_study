def coroutine():
    print('start coroutine')
    while True:
        x = yield
        print(x)
# 파이썬 제너레이터를 이용한 코루틴에서 while문을 사용하면 무한 루프를 구현하고 반복적인 값을 생성할 수 있습니다. 
# 코루틴은 yield 구문에서 일시 중단되어 호출자에게 제어권을 넘겨주기 때문에 while문을 사용해도 계속 yield 값을 받아올 수 있습니다.

# coroutine
# futures
# task
# loop


coro = coroutine()
type(coro)

next(coro)
coro.send(1)

coro.send(55555)
coro.send(11)
coro.send(23)
coro.send(32)