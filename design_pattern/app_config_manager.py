'''
Scenario: Application Config Manager

You're building a backend service. The app reads configuration from environment variables once at startup — database URL, secret key, debug mode. This config must be the same object everywhere in the codebase. Instantiating it twice should return the same instance, not create a fresh one.
Your tasks:

Build a ConfigManager class using __new__ that guarantees only one instance is ever created
Add an __init__ that loads these three values — but only runs once (use an _initialized flag)
Add a get(key: str) method that returns the config value, or raises KeyError with a descriptive message if the key doesn't exist
Add a @classmethod reset() that clears the instance — needed for testing
Write a driver that proves two separate instantiations return the same object using assert inst1 is inst2

Constraints:

Use __new__ — not a module-level variable, not a metaclass
__init__ must not reload config if the instance already exists
Simulate env vars with a plain dict instead of os.environ — hardcode {"DB_URL": "postgres://localhost/app", "SECRET_KEY": "s3cr3t", "DEBUG": "true"}
'''
class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return

        self._initialized = True

        self._config = {
            "DB_URL": "postgres://localhost/app",
            "SECRET_KEY": "s3cr3t",
            "DEBUG": "true"
        }

    def get(self, key: str):
        if key not in self._config:
            raise KeyError(
                f"Config key '{key}' not found. Valid: {list(self._config)}"
            )
        return self._config[key]

    @classmethod
    def reset(cls):
        cls._instance = None


# Driver
inst1 = ConfigManager()
inst2 = ConfigManager()

assert inst1 is inst2

print(inst1.get("DB_URL"))

ConfigManager.reset()

inst3 = ConfigManager()
print(inst1 is inst3)   # False