# Python version: 
 3.13.0

 # Create virtual env ((more info)[https://faun.pub/how-to-install-multiple-python-on-your-mac-d20713740a2d])
 ```pyenv virtualenv 3.13.0 myenv```

 # Activate virtual env
 ```pyenv activate myenv```

 If you have issues activating the virtual env, you can try the following:
 ```
 export PYENV_ROOT="$HOME/.pyenv"
 export PATH="$PYENV_ROOT/bin:$PATH"
 eval "$(pyenv init --path)"
 ```
 ```
 eval "$(pyenv init -)"
 eval "$(pyenv virtualenv-init -)"
 ```

 ## Fix "python not found" in terminal
 ```
 export PYENV_ROOT="$HOME/.pyenv"
 export PATH="$PYENV_ROOT/shims:$PATH"
 ```

 # Install requirements
 ```pip install -r requirements.txt```



## Install py env
url: https://faun.pub/how-to-install-multiple-python-on-your-mac-d20713740a2d