from threading import Thread
from gi.repository import GLib

class TaskHelper:
    def run(self, command, *args, **kwargs):
        thread = Thread(target=self.__run,
                        args=(command, kwargs, *args))
        thread.daemon = True
        thread.start()
        return thread

    def __run(self, command, kwd, *args):
        try:
            result = command(*args)
            if "callback" in kwd.keys():
                (callback, *callback_args) = kwd["callback"]
                if callback is not None:
                    GLib.idle_add(callback, result, *callback_args)
        except Exception as e:
            print(e)
