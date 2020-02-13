package cn.teamthevoid.AiTankArenaServer;

import cn.teamthevoid.AiTankArenaServer.handler.GameServerInitializer;
import cn.teamthevoid.AiTankArenaServer.handler.websocket.ProtoBufToWebSocketBinaryDataEncoder;
import cn.teamthevoid.AiTankArenaServer.handler.websocket.WebSocketBinaryDataDecoder;
import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.room.ServerState;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.http.HttpObjectAggregator;
import io.netty.handler.codec.http.HttpServerCodec;
import io.netty.handler.codec.http.websocketx.WebSocketServerProtocolHandler;
import io.netty.handler.codec.http.websocketx.extensions.compression.WebSocketServerCompressionHandler;
import io.netty.handler.codec.protobuf.ProtobufDecoder;
import io.netty.handler.codec.protobuf.ProtobufEncoder;
import io.netty.handler.codec.protobuf.ProtobufVarint32FrameDecoder;
import io.netty.handler.codec.protobuf.ProtobufVarint32LengthFieldPrepender;
import io.netty.handler.stream.ChunkedWriteHandler;

public class Main {
    ServerState serverState = new ServerState();
    public void run() throws Exception {
        EventLoopGroup socketBossGroup = new NioEventLoopGroup(); // (1)
        EventLoopGroup socketWorkerGroup = new NioEventLoopGroup();
        EventLoopGroup websocketBossGroup = new NioEventLoopGroup(); // (1)
        EventLoopGroup websocketWorkerGroup = new NioEventLoopGroup();
        try {
            ServerBootstrap socketBootstrap = new ServerBootstrap(); // (2)
            socketBootstrap.group(socketBossGroup, socketWorkerGroup)
                    .channel(NioServerSocketChannel.class) // (3)
                    .childHandler(new ChannelInitializer<SocketChannel>() { // (4)
                        @Override
                        public void initChannel(SocketChannel ch) throws Exception {
                            var pipeline = ch.pipeline();
                            pipeline.addLast(new ProtobufVarint32FrameDecoder());
                            pipeline.addLast(new ProtobufDecoder(Operation.getDefaultInstance()));
                            pipeline.addLast(new ProtobufVarint32LengthFieldPrepender());
                            pipeline.addLast(new ProtobufEncoder());
                            pipeline.addLast(new GameServerInitializer(serverState));

//                            pipeline.addLast(new TestOutHandler() );

                        }
                    })
                    .option(ChannelOption.SO_BACKLOG, 128)          // (5)
                    .childOption(ChannelOption.TCP_NODELAY, true);

            ServerBootstrap websocketBootstrap = new ServerBootstrap(); // (2)
            websocketBootstrap.group(websocketBossGroup, websocketWorkerGroup)
                    .channel(NioServerSocketChannel.class) // (3)
                    .childHandler(new ChannelInitializer<SocketChannel>() { // (4)
                        @Override
                        public void initChannel(SocketChannel ch) throws Exception {
                            var pipeline = ch.pipeline();
                            pipeline.addLast(new HttpServerCodec());
                            pipeline.addLast(new HttpObjectAggregator(64 * 1024));
                            pipeline.addLast(new ChunkedWriteHandler());
                            pipeline.addLast(new WebSocketServerCompressionHandler());
                            pipeline.addLast(new WebSocketServerProtocolHandler("/", null, true));
                            pipeline.addLast(new WebSocketBinaryDataDecoder());
                            pipeline.addLast(new ProtobufDecoder(Operation.getDefaultInstance()));
                            pipeline.addLast(new ProtoBufToWebSocketBinaryDataEncoder());
                            pipeline.addLast(new GameServerInitializer(serverState));

//                            pipeline.addLast(new TestOutHandler() );

                        }
                    })
                    .option(ChannelOption.SO_BACKLOG, 128)          // (5)
                    .childOption(ChannelOption.TCP_NODELAY, true);


            ChannelFuture socketFuture = socketBootstrap.bind(8080); // (7)
            ChannelFuture websocketFuture = websocketBootstrap.bind(8081).sync(); // (7)

            socketFuture.channel().closeFuture().sync();
            websocketFuture.channel().closeFuture().sync();
        } finally {
            socketWorkerGroup.shutdownGracefully();
            socketBossGroup.shutdownGracefully();
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().run();
    }
}
