# Hey, I'm Aurik

Computer Engineering student at Queen's University. I build pipelines that pull a real signal out of noisy time series, whether that's brain waves, futures prices or product prices, and then ship them as something people can use.

## What I've built

**[KORE](https://github.com/Aurikology/kore_mvp)**: a cognitive-load wearable. A C++ DSP pipeline, called from Dart over FFI, turns 256 Hz EEG into a theta/alpha Cognitive Load Index using biquad filters, Goertzel band power and Hann windowing. It's parity-tested against a pure-Dart version and checked against public EEG recordings. A signal-quality layer catches electrode faults (contact loss, railing, dropouts) that would otherwise look exactly like cognitive load. The Flutter app runs on Windows and Android. The hardware link is written but not yet tested on a real device; the live stream is simulated.

**[nq-quant](https://github.com/Aurikology/nq-quant)**: an intraday backtester for Nasdaq-100 futures in Python (NumPy, pandas). It detects patterns without look-ahead, uses a deliberately pessimistic fill model, puts bootstrap confidence intervals on returns, runs a permutation test against random entries, and picks parameters in-sample before reporting them out-of-sample. The README reports what the data does and doesn't support.

**[SolGraph](https://github.com/Aurikology/solgraph)**: a read-only Solana assistant. A LangChain agent answers questions about wallets using a graph of wallets, tokens and transfers stored in Apache AGE (Cypher on PostgreSQL). Transfers are worked out from each transaction's balance changes rather than parsed instructions, so swaps are handled correctly. It holds no private keys and can only call an allowlist of read-only tools. Checked against live devnet.

**[Pexi](https://github.com/Aurikology/shin)** (repo: shin): a price-check app with a mascot. Point the phone at something and it tells you whether the price is a steal or a ripoff. TypeScript and Next.js on Vercel, with Gemini for product identification, a 4M+ product catalogue and an iOS build through Capacitor. Built with a cofounder; 900+ commits.

**[128Tick Server Simulation](https://github.com/Aurikology/128Tick-Server-Simulation)**: a C++17 microsecond benchmark of heap allocation against contiguous memory, for 128-tick game-server budgets, using an RAII `std::chrono` timer.

**[SmartCV](https://github.com/Aurikology/SmartCV)**: a team project from the QMIND student AI club at Queen's.

## Tech I work with

`Python` `NumPy` `pandas` `pytest` `C++` `Dart/Flutter` `TypeScript` `JavaScript`

`Next.js` `React` `Node.js` `Electron` `Capacitor` `CMake` `Vercel` `Git`

`LangChain` `Apache AGE` `Cypher` `FastAPI` `Solana`

`DSP` `time series` `backtesting` `statistical testing` `FFI`

## Currently

- Studying Computer Engineering at Queen's
- Building [Pexi](https://my-project-shin.vercel.app) with a cofounder
- Looking for Summer 2027 internships in data science, systems or full-stack engineering

## Get in touch

- **LinkedIn:** [aurikdisler](https://www.linkedin.com/in/aurikdisler/)
- **Email:** aurikdisler@gmail.com
