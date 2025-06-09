# config.py - Configuration for FJCinSA's Crypto Trading Bot
import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import List

# Load environment variables
load_dotenv()

@dataclass
class TradingConfig:
    """Trading configuration settings"""
    bot_name: str = "FJCinSA's Educational Crypto Bot"
    version: str = "1.0.0"
    github_repo: str = "https://github.com/FJCinSA/crypto-trading-bot"
ECHO is off.
    # Safety settings for educational use
    paper_trading: bool = True
    initial_capital: float = 1000.0
    max_risk_per_trade: float = 0.01  # 1%
    max_daily_loss: float = 0.02      # 2%
ECHO is off.
    # Supported trading pairs for learning
    trading_pairs: List[str] = None
ECHO is off.
    def __post_init__(self):
        if self.trading_pairs is None:
            self.trading_pairs = [
                "BTC/USDT",  # Bitcoin
                "ETH/USDT",  # Ethereum
                "ADA/USDT",  # Cardano
                "DOT/USDT",  # Polkadot
            ]

class Config:
    """Main configuration class"""
ECHO is off.
    # Project paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    LOG_DIR = os.path.join(BASE_DIR, "monitoring", "logs")
    MODEL_DIR = os.path.join(BASE_DIR, "data", "models")
ECHO is off.
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/database/trading.db")
ECHO is off.
    # Trading configuration
    TRADING = TradingConfig()
ECHO is off.
    # Environment
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ECHO is off.
    @classmethod
    def create_directories(cls):
        """Create necessary directories"""
        directories = [
            cls.DATA_DIR,
            cls.LOG_DIR,
            cls.MODEL_DIR,
            os.path.join(cls.BASE_DIR, "database"),
        ]
ECHO is off.
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

# Create directories when config is imported
Config.create_directories()
