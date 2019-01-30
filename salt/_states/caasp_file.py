from __future__ import absolute_import


def managed(name, **kwargs):
    '''
    Manage a given file, this function allows for a file to be downloaded from
    the salt master and potentially run through a templating system.

    This is a wrapper on the standard :py:func:`file.managed <salt.states.file.managed>`
    state, as the standard version creates a temporary file in the same directory as `name`,
    and that can lead to some problems with programs/daemons that are watching that
    directory (like the kubelet with `/etc/kubernetes/manifests`).

    For a full list of arguments see :py:func:`file.managed <salt.states.file.managed>`
    '''
    # force the existence of a `check_cmd`, so the regular salt.file.managed()
    # will use a temporary file in `tmp_dir`
    check_cmd = kwargs.pop("check_cmd", "/bin/true")
    tmp_dir = kwargs.pop("tmp_dir", "/tmp")

    return __states__['file.managed'](name=name,
                                      check_cmd=check_cmd,
                                      tmp_dir=tmp_dir,
                                      **kwargs)
