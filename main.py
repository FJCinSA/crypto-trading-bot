# FJCinSA's Educational Crypto Trading Bot - Enhanced Logging Version
# Educational Purpose Only - No Real Money!

import time
import logging
import signal
import sys
from datetime import datetime
from pathlib import Path

class FJCinSACryptoBot:
    """FJCinSA's Educational Crypto Trading Bot with Enhanced Logging"""
    
    def __init__(self):
        self.name = "FJCinSA's Educational Crypto Bot"
        self.version = "1.0.1"  # Updated version
        self.github_repo = "https://github.com/FJCinSA/crypto-trading-bot"
        self.is_running = False
        self.cycle_count = 0
        self.setup_enhanced_logging()
        
    def setup_enhanced_logging(self):
        """Setup enhanced logging configuration with immediate flushing"""
        # Create logs directory
        log_dir = Path("monitoring/logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Clear any existing handlers
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        
        # Create logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # Create file handler with immediate flushing
        file_handler = logging.FileHandler("monitoring/logs/trading.log", mode='a')
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Log system startup
        logging.info("=" * 50)
        logging.info(f"FJCinSA's Crypto Trading Bot v{self.version} - Session Started")
        logging.info("Educational Mode - No Real Money Trading")
        logging.info("=" * 50)
        
        # Force flush to ensure startup logs are written
        for handler in logger.handlers:
            if hasattr(handler, 'flush'):
                handler.flush()
        
    def start(self):
        """Start the educational crypto trading bot"""
        print("=" * 70)
        print(f"🚀 {self.name} v{self.version}")
        print("=" * 70)
        print(f"👨‍💻 Developer: FJCinSA")
        print(f"🌐 Repository: {self.github_repo}")
        print(f"📚 Mode: Educational Learning Only")
        print(f"💰 Money: Paper Trading - No Real Funds")
        print(f"⚠️  Safety: Risk-Free Learning Environment")
        print("=" * 70)
        print()
        
        # Log startup to file
        logging.info(f"Bot startup initiated by FJCinSA")
        logging.info(f"Repository: {self.github_repo}")
        
        try:
            self.is_running = True
            self.main_trading_loop()
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped by user (Ctrl+C)")
            logging.warning("Bot stopped by user interrupt (Ctrl+C)")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            logging.error(f"Bot stopped due to error: {e}")
        finally:
            self.stop()
            
    def main_trading_loop(self):
        """Main educational trading simulation loop"""
        print("🎓 Starting Educational Trading Simulation...")
        print("📖 Learning how professional trading bots work")
        print("-" * 50)
        print()
        
        logging.info("Educational trading simulation starting - 15 cycles planned")
        
        # Educational simulation - 15 cycles
        for cycle in range(15):
            if not self.is_running:
                break
                
            self.cycle_count = cycle + 1
            self.educational_trading_cycle()
            
            # Force log flush after each cycle
            self.flush_logs()
            
            # Wait between cycles (2 seconds for demo)
            time.sleep(2)
            
        logging.info(f"Educational simulation completed - {self.cycle_count} cycles executed")
        self.show_completion_summary()
        
    def educational_trading_cycle(self):
        """Single educational trading cycle with detailed logging"""
        current_time = datetime.now().strftime("%H:%M:%S")
        
        print(f"⏰ {current_time} - Cycle {self.cycle_count}/15")
        
        # Simulate different trading bot activities
        activities = [
            "📊 Fetching real-time market data...",
            "🧠 Analyzing Bitcoin price patterns...",
            "📈 Calculating technical indicators...",
            "🔍 Scanning for trading opportunities...",
            "⚖️  Evaluating risk vs reward ratios...",
            "💼 Optimizing portfolio allocation...",
            "📱 Monitoring news sentiment...",
            "🎯 Calculating optimal position sizes...",
            "📉 Analyzing market trend direction...",
            "🛡️  Checking stop-loss conditions...",
            "💹 Evaluating multiple timeframes...",
            "🔄 Rebalancing portfolio weights...",
            "📋 Updating trading journal...",
            "🚨 Monitoring risk management rules...",
            "🎲 Simulating trade execution..."
        ]
        
        activity = activities[(self.cycle_count - 1) % len(activities)]
        
        # Simulate market data
        btc_price = 45000 + (self.cycle_count * 100) + ((-1) ** self.cycle_count * 500)
        eth_price = 3000 + (self.cycle_count * 50) + ((-1) ** self.cycle_count * 200)
        portfolio_value = 1000 + (self.cycle_count * 5)
        
        # Display cycle information
        print(f"   {activity}")
        print(f"   💰 Paper Portfolio Value: ${portfolio_value:,.2f}")
        print(f"   ₿  Simulated BTC Price: ${btc_price:,.2f}")
        print(f"   ⟠  Simulated ETH Price: ${eth_price:,.2f}")
        print(f"   📊 Learning Progress: {(self.cycle_count/15*100):,.1f}% complete")
        
        # Detailed logging to file
        logging.info(f"CYCLE {self.cycle_count:02d}/15 - {activity}")
        logging.info(f"CYCLE {self.cycle_count:02d} - Portfolio: ${portfolio_value:,.2f}")
        logging.info(f"CYCLE {self.cycle_count:02d} - BTC: ${btc_price:,.2f}, ETH: ${eth_price:,.2f}")
        logging.info(f"CYCLE {self.cycle_count:02d} - Progress: {(self.cycle_count/15*100):,.1f}%")
        
        print()
        
    def flush_logs(self):
        """Force flush all log handlers to ensure immediate file writing"""
        for handler in logging.getLogger().handlers:
            if hasattr(handler, 'flush'):
                handler.flush()
        
    def show_completion_summary(self):
        """Show completion summary and next steps"""
        print("\n" + "=" * 70)
        print("🏆 EDUCATIONAL SIMULATION COMPLETE!")
        print("=" * 70)
        print(f"✅ Completed {self.cycle_count} trading cycles")
        print("✅ Learned how trading bots work in practice")
        print("✅ Understood risk management concepts")
        print("✅ Explored market data analysis")
        print("✅ Gained insight into automated trading")
        print()
        print("📚 What You've Learned:")
        print("   • How trading bots operate in cycles")
        print("   • Basic trading terminology and concepts")
        print("   • Risk management fundamentals")
        print("   • Market data analysis basics")
        print("   • Safe development practices")
        print()
        print("🔜 Recommended Next Steps:")
        print("   1. Study Python programming fundamentals")
        print("   2. Learn about cryptocurrency markets")
        print("   3. Understand technical analysis basics")
        print("   4. Practice with testnet/sandbox APIs")
        print("   5. Build more advanced trading strategies")
        print()
        print("📖 Learning Resources:")
        print("   • Python.org - Learn Python programming")
        print("   • Binance Academy - Crypto education")
        print("   • TradingView - Technical analysis")
        print("   • GitHub - Open source trading projects")
        print()
        print("⚠️  IMPORTANT REMINDERS:")
        print("   • This was educational simulation only")
        print("   • Real trading involves significant financial risk")
        print("   • Never invest more than you can afford to lose")
        print("   • Always use testnet/sandbox for learning")
        print("   • Study extensively before real trading")
        print()
        print(f"🌐 Your Project: {self.github_repo}")
        print("=" * 70)
        
        # Log completion summary
        logging.info("=" * 50)
        logging.info("EDUCATIONAL SIMULATION COMPLETED SUCCESSFULLY")
        logging.info(f"Total cycles executed: {self.cycle_count}")
        logging.info("Summary: FJCinSA successfully completed crypto trading bot simulation")
        logging.info("Next: Ready for advanced learning and development")
        logging.info("=" * 50)
        
    def stop(self):
        """Stop the trading bot safely"""
        self.is_running = False
        logging.info("Educational crypto trading bot stopped by FJCinSA")
        logging.info("Session ended - All systems shutdown safely")
        
        # Final log flush
        self.flush_logs()
        
        print("✅ Bot stopped safely. Thanks for learning with FJCinSA's Crypto Bot!")

def signal_handler(signum, frame):
    """Handle shutdown signals gracefully"""
    print("\n🛑 Received shutdown signal...")
    logging.warning("Bot shutdown via system signal")
    sys.exit(0)

def main():
    """Main entry point"""
    # Setup signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Create and start the educational bot
    bot = FJCinSACryptoBot()
    bot.start()

if __name__ == "__main__":
    main()