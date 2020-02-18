import json
import aioredis
import uuid
import asyncio

async def populate():
    redis = await aioredis.create_redis_pool('redis://localhost')
    
    with open('input.json') as f:
        data = json.load(f)

        for item in data:
            if item['isOut']:
                item_id = uuid.UUID(item['id'])
                print(str(item_id))

                await redis.sadd('lifeoxetine-item:item-ids', item_id.hex)

                if item['isActivated']:
                    print(item['isActivated'])
                    await redis.sadd('lifeoxetine-item:activated-item-ids', item_id.hex)

    redis.close()
    await redis.wait_closed()
    
asyncio.run(populate())
