from spec import skip, Spec, ok_, eq_

from fabric.connection import Connection


class Main(Spec):
    def connection_open_generates_real_connection(self):
        c = Connection('localhost')
        c.open()
        ok_(c.client.get_transport().active)
        eq_(c.is_connected, True)

    def simple_command_on_host(self):
        """
        Run command on host "localhost"
        """
        skip()
        Connection('localhost').run('echo foo')
        # => Result

    def simple_command_on_multiple_hosts(self):
        """
        Run command on localhost...twice!
        """
        skip()
        Batch(['localhost', 'localhost']).run('echo foo')
        # => [Result, Result

    def sudo_command(self):
        """
        Run command via sudo on host "localhost"
        """
        skip()
        Connection('localhost').sudo('echo foo')

    def mixed_sudo_and_normal_commands(self):
        """
        Run command via sudo, and not via sudo, on "localhost"
        """
        skip()
        cxn = Connection('localhost')
        cxn.run('whoami')
        cxn.sudo('whoami')
        # Alternately...
        cxn.run('whoami', runner=Basic)
        cxn.run('whoami', runner=Sudo)

    def switch_command_between_local_and_remote(self):
        """
        Run command truly locally, and over SSH via "localhost"
        """
        # TODO: Only really makes sense at the task level though...
        skip()
        # Basic/raw
        run('hostname') # Or Context().run('hostname')
        Connection('localhost').run('hostname')
