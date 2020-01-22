
package cn.teamthevoid.AiTankArenaServer;

import cn.teamthevoid.AiTankArenaServer.message.People;
import io.netty.buffer.ByteBuf;

import io.netty.buffer.Unpooled;
import io.netty.channel.Channel;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.internal.ChannelUtils;
import io.netty.util.CharsetUtil;

/**
 * Handles a server-side channel.
 */
public class ServerInfoHandler extends ChannelInboundHandlerAdapter { // (1)
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        People buf =(People)msg;
        System.out.println(buf.toString());
        People.Builder builder =People.newBuilder();
        builder.mergeFrom(buf);
        builder.setName("Hello World");
        ctx.writeAndFlush(builder.build());
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) { // (4)
        // Close the connection when an exception is raised.
        cause.printStackTrace();
        ctx.close();
    }
}