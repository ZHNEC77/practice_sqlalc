import asyncio
import os
import sys
from queries.orm import create_tables, insert_data

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

create_tables()
insert_data()

asyncio.run(insert_data())
