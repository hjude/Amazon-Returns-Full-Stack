{ pkgs }: {
    deps = [
        
        pkgs.python39Packages.pip
        pkgs.python39Full
        pkgs.cowsay
        pkgs.python39.pkgs.sqlalchemy 
        pkgs.python39.pkgs.pymysql 
        pkgs.python39.pkgs.flask
        pkgs.python39.pkgs.flask_sqlalchemy
    ];
}