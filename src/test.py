async def on_connect_async(client, userdata, flags_dict, result):
    await client.asyncio_subscribe("RealTimeDataTrasfer/Temperature_S2")

async def on_message_async(client, userdata, msg):
    print(f"Received from {msg.topic}: {str(msg.payload)}")

def connect():
	async with AsyncioPahoClient() as client:
		client.asyncio_listeners.add_on_connect(on_connect_async)
		client.asyncio_listeners.add_on_message(on_message_async)
		await client.asyncio_connect("a9lwl7f2xpfcf-ats.iot.us-east-1.amazonaws.com")



if __name__=="__main__":
	while(True):
		connect()