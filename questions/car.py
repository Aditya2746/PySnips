import asyncio
print('type help for guidelines')

async def main():
    command=''
    started= False
    while True:
        command = input('>> ').lower()
        if command =='start':
            if started:
                print('Car up and running')
            else:
                started = True
                print('Hiting Acelerator')
                await asyncio.sleep(3)
                print('Started')
        elif command =='stop':
            if not started:
                print('Car still')
            else:  
                started = False
                print('Applying brakes')
                await asyncio.sleep(3)
                print('Stopped')
        elif command =='help':
            print(' Type (start) for start')
            print(' Type (stop) for stop')
            print(' Type (quit) for quit')
        elif command =='quit':
            break
        else:
            print("I don't Understand that")

asyncio.run(main())