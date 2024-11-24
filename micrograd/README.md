# Micrograd Implementation

This is an implementation of a tiny autograd engine, following Andrej Karpathy's micrograd tutorial.

## Overview

Micrograd is a small autograd engine that implements backpropagation (reverse-mode autodiff) over a dynamically built DAG. This implementation includes basic operations like addition and multiplication of values, with visualization capabilities.

## Installation

To run this code, you'll need Python 3.9+ and the following dependencies:

- graphviz

You can install the dependencies using brew:

```bash
brew install graphviz
```

To view the generated svg graphs:

- you can use use VSCode extension (Cmd+Shift+X on Mac, or Ctrl+Shift+X on Windows)
- Search for "SVG Preview"
- Install one by SimonSiefke
