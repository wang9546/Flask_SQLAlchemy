from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
class Flask_sqlalchemt_one():
    Integer, String =Integer,String
    def __init__(self,app=None):
        self.app = app
        self.Model = self.make_declarative_base()
        self.Column = Column
        if app is not None:
            self.init_app(app)

    def make_declarative_base(self):
        '''
        Base = declarative_base()
        # 每一次在创建数据表的时候都要做这样一件事
        :return:
        '''
        self.base = declarative_base()
        return self.base


    def init_app(self,app):
        '''
        初始化
        :param app:
        :return:
        '''
        database_url = app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:@127.0.0.1:3306/homework?charset=utf8')
        poll_size = app.config.setdefault('SQLALCHEMY_POOL_SIZE', None)
        print(poll_size)
        poll_timeout = app.config.setdefault('SQLALCHEMY_POOL_TIMEOUT', None)
        track_modifications = app.config.setdefault(
            'SQLALCHEMY_TRACK_MODIFICATIONS', None
        )
        self.engine = self.create_engines(database_url,
                                          max_overflow=0,
                                          pool_size=poll_size,
                                          pool_timeout=poll_timeout,
                                          )
        self.session = self.make_session()
        self.base.query = self.session.query
        @app.teardown_appcontext
        def func(cc):
            '''
            每次请求结束后调用
            :param cc:
            :return:
            '''
            print(11111)

    def create_engines(self,database_url,max_overflow=None,pool_size=None,pool_timeout=None):
        '''
        创建数据库引擎
        :param database_url:
        :param max_overflow:
        :param pool_size:
        :param pool_timeout:
        :return:
        '''
        engine = create_engine(
            database_url,
            max_overflow=max_overflow,
            pool_size=pool_size,
            pool_timeout=pool_timeout,
        )
        return engine

    def make_session(self):
        '''
        session会话
        :return:
        '''
        Session = sessionmaker(self.engine)
        db_sesson = scoped_session(Session)
        return db_sesson

    def create_all(self):
        self.Model.metadata.create_all(self.engine)
        return

db = Flask_sqlalchemt_one()

class User(db.Model):
    '''
    model表
    '''
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(16),nullable=False)

