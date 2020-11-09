from petisco import Event
from petisco.event.legacy.subscriber.domain.subscriber_handler import subscriber_handler


@subscriber_handler()
def send_notification(event: Event):
    print(f"Event: {event}")
