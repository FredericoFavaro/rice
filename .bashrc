#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias vim='nvim'
alias hx='helix'
alias pacS='sudo pacman -S'
alias sshgh='ssh-add $HOME/.ssh/github'

#exec thunar --daemon

[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx
#if [ -z "$DISPLAY" ] && [ "$XDG_VTNR" = 1 ]; then
#  exec startx
#fi

if ! pgrep -u "$USER" ssh-agent > /dev/null; then
    ssh-agent -t 1h > "$XDG_RUNTIME_DIR/ssh-agent.env"
fi
if [[ ! -f "$SSH_AUTH_SOCK" ]]; then
    source "$XDG_RUNTIME_DIR/ssh-agent.env" >/dev/null
fi


#export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"

#PS1='[\u@\h \W]\$ '

PS1='\w ➡ '

# dando erros de render
#PS1="\e[1;34m\w \e[0;32m➡\[\033[0m\] "

## NODEJS
#export NVM_DIR="$HOME/.config/nvm"
#[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
#[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
#
### Seleciona automaticamente a versao do node usado no projeto com base no arquivo .nvmrc
#cdnvm() {
#    command cd "$@" || return $?
#    nvm_path="$(nvm_find_up .nvmrc | command tr -d '\n')"
#
#    # If there are no .nvmrc file, use the default nvm version
#    if [[ ! $nvm_path = *[^[:space:]]* ]]; then
#
#        declare default_version
#        default_version="$(nvm version default)"
#
#        # If there is no default version, set it to `node`
#        # This will use the latest version on your machine
#        if [ $default_version = 'N/A' ]; then
#            nvm alias default node
#            default_version=$(nvm version default)
#        fi
#
#        # If the current version is not the default version, set it to use the default version
#        if [ "$(nvm current)" != "${default_version}" ]; then
#            nvm use default
#        fi
#    elif [[ -s "${nvm_path}/.nvmrc" && -r "${nvm_path}/.nvmrc" ]]; then
#        declare nvm_version
#        nvm_version=$(<"${nvm_path}"/.nvmrc)
#
#        declare locally_resolved_nvm_version
#        # `nvm ls` will check all locally-available versions
#        # If there are multiple matching versions, take the latest one
#        # Remove the `->` and `*` characters and spaces
#        # `locally_resolved_nvm_version` will be `N/A` if no local versions are found
#        locally_resolved_nvm_version=$(nvm ls --no-colors "${nvm_version}" | command tail -1 | command tr -d '\->*' | command tr -d '[:space:]')
#
#        # If it is not already installed, install it
#        # `nvm install` will implicitly use the newly-installed version
#        if [ "${locally_resolved_nvm_version}" = 'N/A' ]; then
#            nvm install "${nvm_version}";
#        elif [ "$(nvm current)" != "${locally_resolved_nvm_version}" ]; then
#            nvm use "${nvm_version}";
#        fi
#    fi
#}

#alias cd='cdnvm'
#cdnvm "$PWD" || exit

export LIBVA_DRIVER_NAME=i965
export VDPAU_DRIVER=va_gl
