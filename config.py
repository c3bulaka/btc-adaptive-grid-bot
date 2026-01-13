"""
Centralized Configuration Module for BTC Adaptive Grid Bot
Manages all configuration settings for the trading bot including
API keys, trading parameters, grid settings, and logging configurations.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from enum import Enum


class TradingMode(Enum):
    """Trading mode enumeration"""
    LIVE = "live"
    PAPER = "paper"
    BACKTEST = "backtest"


class GridStrategy(Enum):
    """Grid strategy enumeration"""
    FIXED = "fixed"
    ADAPTIVE = "adaptive"
    DYNAMIC = "dynamic"


@dataclass
class APIConfig:
    """API Configuration"""
    exchange: str = os.getenv("EXCHANGE", "binance")
    api_key: str = os.getenv("API_KEY", "")
    api_secret: str = os.getenv("API_SECRET", "")
    api_passphrase: Optional[str] = os.getenv("API_PASSPHRASE")
    testnet: bool = os.getenv("USE_TESTNET", "false").lower() == "true"
    
    def validate(self) -> bool:
        """Validate API configuration"""
        if not self.api_key or not self.api_secret:
            raise ValueError("API_KEY and API_SECRET must be configured")
        return True


@dataclass
class GridConfig:
    """Grid Trading Configuration"""
    # Grid parameters
    grid_levels: int = int(os.getenv("GRID_LEVELS", "10"))
    lower_bound: float = float(os.getenv("GRID_LOWER_BOUND", "35000"))
    upper_bound: float = float(os.getenv("GRID_UPPER_BOUND", "45000"))
    
    # Order sizing
    order_size: float = float(os.getenv("ORDER_SIZE", "0.01"))  # BTC amount per order
    use_percentage_allocation: bool = os.getenv("USE_PERCENTAGE_ALLOCATION", "true").lower() == "true"
    allocation_percentage: float = float(os.getenv("ALLOCATION_PERCENTAGE", "100"))
    
    # Strategy settings
    strategy: GridStrategy = GridStrategy.ADAPTIVE
    enable_profit_taking: bool = os.getenv("ENABLE_PROFIT_TAKING", "true").lower() == "true"
    profit_margin_percent: float = float(os.getenv("PROFIT_MARGIN_PERCENT", "0.5"))
    
    # Adaptive parameters
    enable_adaptive_pricing: bool = os.getenv("ENABLE_ADAPTIVE_PRICING", "true").lower() == "true"
    volatility_adjustment_factor: float = float(os.getenv("VOLATILITY_ADJUSTMENT", "1.0"))
    adaptation_interval_seconds: int = int(os.getenv("ADAPTATION_INTERVAL", "300"))
    
    def calculate_grid_spacing(self) -> float:
        """Calculate spacing between grid levels"""
        return (self.upper_bound - self.lower_bound) / (self.grid_levels - 1)
    
    def get_grid_levels(self) -> list:
        """Generate list of grid price levels"""
        spacing = self.calculate_grid_spacing()
        return [self.lower_bound + (i * spacing) for i in range(self.grid_levels)]


@dataclass
class TradingConfig:
    """Trading Configuration"""
    mode: TradingMode = TradingMode.PAPER
    symbol: str = os.getenv("TRADING_SYMBOL", "BTCUSDT")
    base_asset: str = "BTC"
    quote_asset: str = "USDT"
    
    # Risk management
    max_position_size: float = float(os.getenv("MAX_POSITION_SIZE", "1.0"))  # BTC
    max_open_orders: int = int(os.getenv("MAX_OPEN_ORDERS", "50"))
    stop_loss_percent: float = float(os.getenv("STOP_LOSS_PERCENT", "5.0"))
    
    # Fees
    maker_fee_percent: float = float(os.getenv("MAKER_FEE", "0.1"))
    taker_fee_percent: float = float(os.getenv("TAKER_FEE", "0.1"))
    
    # Order settings
    order_timeout_seconds: int = int(os.getenv("ORDER_TIMEOUT", "300"))
    min_order_value_usdt: float = float(os.getenv("MIN_ORDER_VALUE", "10"))


@dataclass
class LoggingConfig:
    """Logging Configuration"""
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: str = os.getenv("LOG_FILE", "bot.log")
    log_dir: str = os.getenv("LOG_DIR", "logs")
    max_log_size_mb: int = int(os.getenv("MAX_LOG_SIZE_MB", "10"))
    backup_count: int = int(os.getenv("LOG_BACKUP_COUNT", "5"))
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    enable_console_logging: bool = os.getenv("ENABLE_CONSOLE_LOGGING", "true").lower() == "true"
    enable_file_logging: bool = os.getenv("ENABLE_FILE_LOGGING", "true").lower() == "true"


@dataclass
class MonitoringConfig:
    """Monitoring and Alerts Configuration"""
    enable_monitoring: bool = os.getenv("ENABLE_MONITORING", "true").lower() == "true"
    heartbeat_interval_seconds: int = int(os.getenv("HEARTBEAT_INTERVAL", "60"))
    
    # Webhook alerts
    enable_webhooks: bool = os.getenv("ENABLE_WEBHOOKS", "false").lower() == "true"
    webhook_url: Optional[str] = os.getenv("WEBHOOK_URL")
    webhook_events: list = field(default_factory=lambda: [
        "order_filled",
        "grid_rebalanced",
        "position_updated",
        "error_occurred"
    ])
    
    # Metrics
    collect_metrics: bool = os.getenv("COLLECT_METRICS", "true").lower() == "true"
    metrics_interval_seconds: int = int(os.getenv("METRICS_INTERVAL", "300"))


@dataclass
class DatabaseConfig:
    """Database Configuration"""
    enable_persistence: bool = os.getenv("ENABLE_PERSISTENCE", "true").lower() == "true"
    db_type: str = os.getenv("DB_TYPE", "sqlite")  # sqlite, postgresql, mongodb
    db_path: str = os.getenv("DB_PATH", "data/bot.db")
    db_host: Optional[str] = os.getenv("DB_HOST")
    db_port: Optional[int] = int(os.getenv("DB_PORT", "5432")) if os.getenv("DB_PORT") else None
    db_name: str = os.getenv("DB_NAME", "adaptive_grid_bot")
    db_user: Optional[str] = os.getenv("DB_USER")
    db_password: Optional[str] = os.getenv("DB_PASSWORD")
    
    # Backup settings
    enable_backups: bool = os.getenv("ENABLE_BACKUPS", "true").lower() == "true"
    backup_interval_hours: int = int(os.getenv("BACKUP_INTERVAL_HOURS", "24"))


@dataclass
class BacktestConfig:
    """Backtesting Configuration"""
    enable_backtesting: bool = False
    start_date: str = os.getenv("BACKTEST_START_DATE", "2023-01-01")
    end_date: str = os.getenv("BACKTEST_END_DATE", "2024-01-01")
    initial_capital: float = float(os.getenv("BACKTEST_INITIAL_CAPITAL", "10000"))
    data_source: str = os.getenv("BACKTEST_DATA_SOURCE", "binance")
    timeframe: str = os.getenv("BACKTEST_TIMEFRAME", "1h")


class Config:
    """Main Configuration Manager"""
    
    def __init__(self):
        """Initialize all configuration sections"""
        self.api = APIConfig()
        self.grid = GridConfig()
        self.trading = TradingConfig()
        self.logging = LoggingConfig()
        self.monitoring = MonitoringConfig()
        self.database = DatabaseConfig()
        self.backtest = BacktestConfig()
        
        # Application settings
        self.app_name = "BTC Adaptive Grid Bot"
        self.version = os.getenv("APP_VERSION", "1.0.0")
        self.debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"
        
    def validate(self) -> bool:
        """Validate all configurations"""
        try:
            self.api.validate()
            return True
        except ValueError as e:
            raise ValueError(f"Configuration validation failed: {str(e)}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            "api": {
                "exchange": self.api.exchange,
                "testnet": self.api.testnet,
            },
            "grid": {
                "levels": self.grid.grid_levels,
                "lower_bound": self.grid.lower_bound,
                "upper_bound": self.grid.upper_bound,
                "strategy": self.grid.strategy.value,
            },
            "trading": {
                "mode": self.trading.mode.value,
                "symbol": self.trading.symbol,
                "max_position_size": self.trading.max_position_size,
            },
            "app": {
                "name": self.app_name,
                "version": self.version,
                "debug": self.debug_mode,
            },
        }
    
    def get_grid_levels(self) -> list:
        """Get calculated grid price levels"""
        return self.grid.get_grid_levels()


# Global configuration instance
config = Config()


# Convenience functions
def get_config() -> Config:
    """Get global configuration instance"""
    return config


def get_grid_levels() -> list:
    """Get grid price levels"""
    return config.get_grid_levels()


def is_live_trading() -> bool:
    """Check if trading mode is live"""
    return config.trading.mode == TradingMode.LIVE


def is_paper_trading() -> bool:
    """Check if trading mode is paper"""
    return config.trading.mode == TradingMode.PAPER


def is_backtesting() -> bool:
    """Check if mode is backtesting"""
    return config.trading.mode == TradingMode.BACKTEST


if __name__ == "__main__":
    # Print configuration for debugging
    cfg = get_config()
    print(f"Application: {cfg.app_name} v{cfg.version}")
    print(f"Trading Mode: {cfg.trading.mode.value}")
    print(f"Exchange: {cfg.api.exchange}")
    print(f"Symbol: {cfg.trading.symbol}")
    print(f"Grid Levels: {cfg.grid.grid_levels}")
    print(f"Grid Range: {cfg.grid.lower_bound} - {cfg.grid.upper_bound}")
    print(f"Grid Spacing: {cfg.grid.calculate_grid_spacing():.2f}")
