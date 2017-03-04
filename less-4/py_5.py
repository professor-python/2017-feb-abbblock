import asyncio

# python 3.5+
async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(0.0001) # как yield from
        f *= i
    print("Task %s: RESULT: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factorial("A", 20),
    factorial("B", 30),
    factorial("C", 40),
))
loop.close()
