//
// List.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation

@objc public class List: NSObject, Codable {

    public var _123list: String?

    public init(_123list: String? = nil) {
        self._123list = _123list
    }

    public enum CodingKeys: String, CodingKey, CaseIterable {
        case _123list = "123-list"
    }

}
