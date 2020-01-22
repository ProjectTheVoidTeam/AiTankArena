
package cn.teamthevoid.AiTankArenaServer;

import cn.teamthevoid.AiTankArenaServer.message.Operation;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

/**
 * Handles a server-side channel.
 */
public class ServerInfoHandler extends ChannelInboundHandlerAdapter { // (1)
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        Operation buf = (Operation) msg;
        System.out.println(buf.toString());
//        People.Builder builder =People.newBuilder();
//        builder.mergeFrom(buf);
//        builder.setName("Hello World");
        ctx.writeAndFlush(buf);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) { // (4)
        // Close the connection when an exception is raised.
        cause.printStackTrace();
        ctx.close();
    }
}