# Template project for developing PySide6 applications

## Features

1. Include tools for both compiling UI, design forms, and do translation
1. Clean design/seperation for widgets and ui files
1. ready-to-use VSCode tasks and debug configurations

## Getting started

1. clone this repo
1. install uv/ruff: [UV](https://docs.astral.sh/uv/getting-started/)
1. run `uv sync`
1. run debug config "Main" in VS Code (or code-oss/vscodium)

## Design Forms

1. Run task "Design Forms"
1. after create a new form don't forget to create a new file in `widgets` directory to load the form

## Do Translation
1. Run task "Do Translation"
1. After closed Linguist the `qm` file will be automatically updated
1. Due to a bug (linguist freeze) in Windows platform we recommend using MSYS2 linguist in Windows:

    1. install [MSYS2](https://www.msys2.org/)
    1. install package `ucrt64/mingw-w64-ucrt-x86_64-qt6-tools` using `pacman`:
    ```
        pacman -Syu
        pacman -S ucrt64/mingw-w64-ucrt-x86_64-qt6-tools
    ```

## Build release

1. Run task "Build Release".
 This will use `pyinstaller` to package all the dependencies.
