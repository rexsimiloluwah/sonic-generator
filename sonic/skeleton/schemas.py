"""
    schemas.py : Create schemas for pydantic based data validation for your API endpoints
"""
from typing import List, Optional
from pydantic import BaseModel, constr, EmailStr
from datetime import datetime
from enum import Enum