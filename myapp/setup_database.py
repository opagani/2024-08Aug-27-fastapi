#!/usr/bin/env python3

import asyncio
import aiosqlite

async def main():
    async with aiosqlite.connect('apiapp.db') as db:
        await db.execute('''
        CREATE TABLE People(
            id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            shoe_size INTEGER
        );
        ''')

        await db.execute(f"""
        INSERT INTO People (id, first_name, last_name, shoe_size)
        VALUES
          (1, 'Reuven', 'Lerner', 46),
          (2, 'Atara', 'Lerner-Friedman', 40),
          (3, 'Shikma', 'Lerner-Friedman', 40),
          (4, 'Amotz', 'Lerner-Friedman', 46)
        """)
        await db.commit()

if __name__ == '__main__':
    asyncio.run(main())
