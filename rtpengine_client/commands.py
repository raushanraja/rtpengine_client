from abc import ABC, abstractmethod
from enum import Enum

from encoder import encode


class CommandEnum(Enum):
    PING = 'ping'
    OFFER = 'offer'
    ANSWER = 'answer'
    DELETE = 'delete'
    QUERY = 'query'
    CALL_LIST = 'list'
    START_RECORDING = 'start recording'
    STOP_RECORDING = 'stop recording'
    PAUSE_RECORDING = 'pause recording'
    BLOCK_DTMF = 'block DTMF'
    UNBLOCK_DTMF = 'unblock DTMF'
    BLOCK_MEDIA = 'block media'
    UNBLOCK_MEDIA = 'unblock media'
    SILENCE_MEDIA = 'silence media'
    UNSILENCE_MEDIA = 'unsilence media'
    START_FORWARDING = 'start forwarding'
    STOP_FORWARDING = 'stop forwarding'
    PLAY_MEDIA = 'play media'
    STOP_MEDIA = 'stop media'
    PLAY_DTMF = 'play DTMF'
    STATISTICS = 'statistics'
    PUBLISH = 'publish'
    SUBSCRIBE_REQUEST = 'subscribe request'
    SUBSCRIBE_ANSWER = 'subscribe answer'
    UNSUBSCRIBE = 'unsubscribe'


class CommandBase(ABC):

    @abstractmethod
    def build(self, *args, **kwargs):
        raise NotImplementedError()


class CallList(CommandBase):
    command = CommandEnum.CALL_LIST

    def build(self):
        data = {'command': self.command.value}
        return encode(data)


class Ping(CommandBase):
    command = CommandEnum.PING

    def build(self):
        data = {'command': self.command.value}
        return encode(data)


class CommandFactory:
    commands = {
        CommandEnum.PING: Ping(),
        CommandEnum.CALL_LIST: CallList()
    }

    def get_command(self, command_type: CommandEnum):
        if isinstance(command_type, CommandEnum):
            return CommandFactory.commands.get(command_type, None)
