from pathlib import Path
from loguru import logger

def setup_logging(log_file: str | None = None) -> None:
    """配置 loguru 日志输出到控制台与文件。

    Args:
        log_file: 可选，日志文件路径。默认写入 data/logs/ds_factory.log
    """
    log_dir = Path("data/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    logfile = Path(log_file) if log_file else log_dir / "ds_factory.log"

    # 清理默认 handler，避免重复
    logger.remove()
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level="INFO",
        backtrace=False,
        diagnose=False,
        colorize=True,
    )
    logger.add(
        logfile,
        level="DEBUG",
        rotation="10 MB",
        retention="10 days",
        compression="gz",
        enqueue=True,
        backtrace=False,
        diagnose=False,
    )
    logger.debug(f"Logging initialized. File: {logfile}")
