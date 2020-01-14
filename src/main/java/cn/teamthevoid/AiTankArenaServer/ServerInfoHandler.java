
package cn.teamthevoid.AiTankArenaServer;

import io.netty.buffer.ByteBuf;

import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.internal.ChannelUtils;
import io.netty.util.CharsetUtil;

/**
 * Handles a server-side channel.
 */
public class ServerInfoHandler extends ChannelInboundHandlerAdapter { // (1)


    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        var str="AiTankAreanaServer Version:0.0.1";
        var buf = Unpooled.copiedBuffer(str, CharsetUtil.UTF_8);
        ctx.writeAndFlush(buf);
    }

    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) throws Exception {

    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) { // (4)
        // Close the connection when an exception is raised.
        cause.printStackTrace();
        ctx.close();
    }
}