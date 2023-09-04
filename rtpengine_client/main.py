import asyncio
from config.env import env
from client import AioHttpClient
import logging

from commands import CallList, CommandBase, CommandEnum, CommandFactory
from encoder import decode, encode


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

cf = CommandFactory()


async def main():
    headers = {"content-type": "application/x-rtpengine-ng"}
    client = AioHttpClient(env.RTPENGINE_URL, headers=headers)

    command:CallList = cf.get_command(CommandEnum.CALL_LIST)
    if command:
        response = await client.post(command.build())
        log.info(command.decode(response))

    command = cf.get_command(CommandEnum.PING)
    if command:
        response = await client.post(command.build())
        log.info(command.decode(response))

    # command = cf.get_command(CommandEnum.STATISTICS)
    # if command:
    #     response = await client.post(command.build())
    #     log.info(decode(response))

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
