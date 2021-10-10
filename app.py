from quart import Quart

from db import async_session

# Instantiate app for ASGI
app = Quart(__name__)

@app.route('/1/health')
async def health():
    async with async_session() as session:
        result = (await session.execute('SELECT 1')).fetchone()
    return 'OK' if result[0] else 'DOWN'
    

# Start the server
if __name__ == '__main__':
    app.run()
