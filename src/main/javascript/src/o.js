"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.default = exports.AiTankArenaServer = undefined;

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) {
    return typeof obj;
} : function (obj) {
    return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj;
}; /*eslint-disable block-scoped-var, id-length, no-control-regex, no-magic-numbers, no-prototype-builtins, no-redeclare, no-shadow, no-var, sort-vars*/


var _minimal = require("protobufjs/minimal");

var $protobuf = _interopRequireWildcard(_minimal);

function _interopRequireWildcard(obj) {
    if (obj && obj.__esModule) {
        return obj;
    } else {
        var newObj = {};
        if (obj != null) {
            for (var key in obj) {
                if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key];
            }
        }
        newObj.default = obj;
        return newObj;
    }
}

// Common aliases
var $Reader = $protobuf.Reader,
    $Writer = $protobuf.Writer,
    $util = $protobuf.util;

// Exported root namespace
var $root = $protobuf.roots["default"] || ($protobuf.roots["default"] = {});

var AiTankArenaServer = exports.AiTankArenaServer = $root.AiTankArenaServer = function () {

    /**
     * Namespace AiTankArenaServer.
     * @exports AiTankArenaServer
     * @namespace
     */
    var AiTankArenaServer = {};

    /**
     * OperationType enum.
     * @name AiTankArenaServer.OperationType
     * @enum {string}
     * @property {number} GET_STATUS=0 GET_STATUS value
     * @property {number} JOIN=1 JOIN value
     * @property {number} AI_ACTION=2 AI_ACTION value
     * @property {number} FRANCE=3 FRANCE value
     * @property {number} HALT=4 HALT value
     * @property {number} INIT=5 INIT value
     * @property {number} REJOIN=6 REJOIN value
     * @property {number} SERVER_INFO=7 SERVER_INFO value
     */
    AiTankArenaServer.OperationType = function () {
        var valuesById = {},
            values = Object.create(valuesById);
        values[valuesById[0] = "GET_STATUS"] = 0;
        values[valuesById[1] = "JOIN"] = 1;
        values[valuesById[2] = "AI_ACTION"] = 2;
        values[valuesById[3] = "FRANCE"] = 3;
        values[valuesById[4] = "HALT"] = 4;
        values[valuesById[5] = "INIT"] = 5;
        values[valuesById[6] = "REJOIN"] = 6;
        values[valuesById[7] = "SERVER_INFO"] = 7;
        return values;
    }();

    AiTankArenaServer.Operation = function () {

        /**
         * Properties of an Operation.
         * @memberof AiTankArenaServer
         * @interface IOperation
         * @property {AiTankArenaServer.OperationType|null} [type] Operation type
         * @property {string|null} [message] Operation message
         */

        /**
         * Constructs a new Operation.
         * @memberof AiTankArenaServer
         * @classdesc Represents an Operation.
         * @implements IOperation
         * @constructor
         * @param {AiTankArenaServer.IOperation=} [properties] Properties to set
         */
        function Operation(properties) {
            if (properties) for (var keys = Object.keys(properties), i = 0; i < keys.length; ++i) {
                if (properties[keys[i]] != null) this[keys[i]] = properties[keys[i]];
            }
        }

        /**
         * Operation type.
         * @member {AiTankArenaServer.OperationType} type
         * @memberof AiTankArenaServer.Operation
         * @instance
         */
        Operation.prototype.type = 0;

        /**
         * Operation message.
         * @member {string} message
         * @memberof AiTankArenaServer.Operation
         * @instance
         */
        Operation.prototype.message = "";

        /**
         * Creates a new Operation instance using the specified properties.
         * @function create
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {AiTankArenaServer.IOperation=} [properties] Properties to set
         * @returns {AiTankArenaServer.Operation} Operation instance
         */
        Operation.create = function create(properties) {
            return new Operation(properties);
        };

        /**
         * Encodes the specified Operation message. Does not implicitly {@link AiTankArenaServer.Operation.verify|verify} messages.
         * @function encode
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {AiTankArenaServer.IOperation} message Operation message or plain object to encode
         * @param {$protobuf.Writer} [writer] Writer to encode to
         * @returns {$protobuf.Writer} Writer
         */
        Operation.encode = function encode(message, writer) {
            if (!writer) writer = $Writer.create();
            if (message.type != null && message.hasOwnProperty("type")) writer.uint32( /* id 1, wireType 0 =*/8).int32(message.type);
            if (message.message != null && message.hasOwnProperty("message")) writer.uint32( /* id 2, wireType 2 =*/18).string(message.message);
            return writer;
        };

        /**
         * Encodes the specified Operation message, length delimited. Does not implicitly {@link AiTankArenaServer.Operation.verify|verify} messages.
         * @function encodeDelimited
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {AiTankArenaServer.IOperation} message Operation message or plain object to encode
         * @param {$protobuf.Writer} [writer] Writer to encode to
         * @returns {$protobuf.Writer} Writer
         */
        Operation.encodeDelimited = function encodeDelimited(message, writer) {
            return this.encode(message, writer).ldelim();
        };

        /**
         * Decodes an Operation message from the specified reader or buffer.
         * @function decode
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {$protobuf.Reader|Uint8Array} reader Reader or buffer to decode from
         * @param {number} [length] Message length if known beforehand
         * @returns {AiTankArenaServer.Operation} Operation
         * @throws {Error} If the payload is not a reader or valid buffer
         * @throws {$protobuf.util.ProtocolError} If required fields are missing
         */
        Operation.decode = function decode(reader, length) {
            if (!(reader instanceof $Reader)) reader = $Reader.create(reader);
            var end = length === undefined ? reader.len : reader.pos + length,
                message = new $root.AiTankArenaServer.Operation();
            while (reader.pos < end) {
                var tag = reader.uint32();
                switch (tag >>> 3) {
                    case 1:
                        message.type = reader.int32();
                        break;
                    case 2:
                        message.message = reader.string();
                        break;
                    default:
                        reader.skipType(tag & 7);
                        break;
                }
            }
            return message;
        };

        /**
         * Decodes an Operation message from the specified reader or buffer, length delimited.
         * @function decodeDelimited
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {$protobuf.Reader|Uint8Array} reader Reader or buffer to decode from
         * @returns {AiTankArenaServer.Operation} Operation
         * @throws {Error} If the payload is not a reader or valid buffer
         * @throws {$protobuf.util.ProtocolError} If required fields are missing
         */
        Operation.decodeDelimited = function decodeDelimited(reader) {
            if (!(reader instanceof $Reader)) reader = new $Reader(reader);
            return this.decode(reader, reader.uint32());
        };

        /**
         * Verifies an Operation message.
         * @function verify
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {Object.<string,*>} message Plain object to verify
         * @returns {string|null} `null` if valid, otherwise the reason why it is not
         */
        Operation.verify = function verify(message) {
            if ((typeof message === "undefined" ? "undefined" : _typeof(message)) !== "object" || message === null) return "object expected";
            if (message.type != null && message.hasOwnProperty("type")) switch (message.type) {
                default:
                    return "type: enum value expected";
                case 0:
                case 1:
                case 2:
                case 3:
                case 4:
                case 5:
                case 6:
                case 7:
                    break;
            }
            if (message.message != null && message.hasOwnProperty("message")) if (!$util.isString(message.message)) return "message: string expected";
            return null;
        };

        /**
         * Creates an Operation message from a plain object. Also converts values to their respective internal types.
         * @function fromObject
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {Object.<string,*>} object Plain object
         * @returns {AiTankArenaServer.Operation} Operation
         */
        Operation.fromObject = function fromObject(object) {
            if (object instanceof $root.AiTankArenaServer.Operation) return object;
            var message = new $root.AiTankArenaServer.Operation();
            switch (object.type) {
                case "GET_STATUS":
                case 0:
                    message.type = 0;
                    break;
                case "JOIN":
                case 1:
                    message.type = 1;
                    break;
                case "AI_ACTION":
                case 2:
                    message.type = 2;
                    break;
                case "FRANCE":
                case 3:
                    message.type = 3;
                    break;
                case "HALT":
                case 4:
                    message.type = 4;
                    break;
                case "INIT":
                case 5:
                    message.type = 5;
                    break;
                case "REJOIN":
                case 6:
                    message.type = 6;
                    break;
                case "SERVER_INFO":
                case 7:
                    message.type = 7;
                    break;
            }
            if (object.message != null) message.message = String(object.message);
            return message;
        };

        /**
         * Creates a plain object from an Operation message. Also converts values to other types if specified.
         * @function toObject
         * @memberof AiTankArenaServer.Operation
         * @static
         * @param {AiTankArenaServer.Operation} message Operation
         * @param {$protobuf.IConversionOptions} [options] Conversion options
         * @returns {Object.<string,*>} Plain object
         */
        Operation.toObject = function toObject(message, options) {
            if (!options) options = {};
            var object = {};
            if (options.defaults) {
                object.type = options.enums === String ? "GET_STATUS" : 0;
                object.message = "";
            }
            if (message.type != null && message.hasOwnProperty("type")) object.type = options.enums === String ? $root.AiTankArenaServer.OperationType[message.type] : message.type;
            if (message.message != null && message.hasOwnProperty("message")) object.message = message.message;
            return object;
        };

        /**
         * Converts this Operation to JSON.
         * @function toJSON
         * @memberof AiTankArenaServer.Operation
         * @instance
         * @returns {Object.<string,*>} JSON object
         */
        Operation.prototype.toJSON = function toJSON() {
            return this.constructor.toObject(this, $protobuf.util.toJSONOptions);
        };

        return Operation;
    }();

    return AiTankArenaServer;
}();

exports.default = $root;
